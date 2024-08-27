#!/usr/bin/env node
import express from "express";
import redis from "redis";
import kue from "kue";
import { promisify } from "util";

const app = express();
const port = 1245;

const client = redis.createClient();
const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);

const queue = kue.createQueue();

const INITIAL_SEATS = 50;
let reservationEnabled = true;

const reserveSeat = async (number) => {
  await setAsync("available_seats", number);
};

const getCurrentAvailableSeats = async () => {
  const seats = await getAsync("available_seats");
  return seats ? parseInt(seats, 10) : null;
};

reserveSeat(INITIAL_SEATS);

app.get("/available_seats", async (req, res) => {
  const availableSeats = await getCurrentAvailableSeats();
  res.json({ numberOfAvailableSeats: availableSeats.toString() });
});

app.get("/reserve_seat", async (req, res) => {
  if (!reservationEnabled) {
    return res.json({ status: "Reservations are blocked" });
  }

  const job = queue.create("reserve_seat").save((err) => {
    if (!err) {
      return res.json({ status: "Reservation in process" });
    }
    res.json({ status: "Reservation failed" });
  });

  job.on("complete", () => {
    console.log(`Seat reservation job ${job.id} completed`);
  });

  job.on("failed", (err) => {
    console.log(`Seat reservation job ${job.id} failed: ${err}`);
  });
});

app.get("/process", async (req, res) => {
  res.json({ status: "Queue processing" });

  const processQueue = async () => {
    queue.process("reserve_seat", async (job, done) => {
      const currentSeats = await getCurrentAvailableSeats();

      if (currentSeats === null) {
        done(new Error("Failed to retrieve available seats"));
        return;
      }

      if (currentSeats <= 0) {
        reservationEnabled = false;
        done(new Error("Not enough seats available"));
        return;
      }

      await reserveSeat(currentSeats - 1);
      done();
    });
  };

  processQueue();
});

app.listen(port, () => {
  console.log(`Server running on port ${port}`);
});
