#!/usr/bin/node
import redis from "redis";
import { promisify } from "util";

const client = redis.createClient();

client.on("connect", () => {
  console.log("Redis client connected to the server");
});

client.on("error", (error) => {
  console.log(`Redis client not connected to the server: ${error.message}`);
});

const getAsync = promisify(client.get).bind(client);

const setNewSchool = (schoolName, value) => {
  client.set(schoolName, value, redis.print);
};

const displaySchoolValue = async (schoolName) => {
  try {
    const result = await getAsync(schoolName);
    console.log(result);
  } catch (error) {
    console.log(error);
  }
};

displaySchoolValue("Holberton");
setNewSchool("HolbertonSanFrancisco", "100");
displaySchoolValue("HolbertonSanFrancisco");
