#!/usr/bin/node
import kue from "kue";

const queue = kue.createQueue();
const jobData = {
  phoneNumber: "5678922039",
  message: "lorem ipsum",
};

const job = queue.createJob("push_notification_code", jobData).save((error) => {
  if (!error) {
    console.log(`Notification job created: ${job.id}`);
  } else {
    console.error(`Failed to create job: ${err.message}`);
  }
});

job.on("complete", () => {
  console.log("Notification job completed");
});

job.on("failed", () => {
  console.log("Notification job failed");
});
