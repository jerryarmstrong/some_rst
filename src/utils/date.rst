src/utils/date.ts
=================

Last edited: 2022-08-30 20:54:29

Contents:

.. code-block:: ts

    export function displayTimestamp(
  unixTimestamp: number,
  shortTimeZoneName = false
): string {
  const expireDate = new Date(unixTimestamp);
  const dateString = new Intl.DateTimeFormat("en-US", {
    year: "numeric",
    month: "short",
    day: "numeric",
  }).format(expireDate);
  const timeString = new Intl.DateTimeFormat("en-US", {
    hour: "numeric",
    minute: "numeric",
    second: "numeric",
    hourCycle: "h23",
    timeZoneName: shortTimeZoneName ? "short" : "long",
  }).format(expireDate);
  return `${dateString} at ${timeString}`;
}

export function displayTimestampUtc(
  unixTimestamp: number,
  shortTimeZoneName = false
): string {
  const expireDate = new Date(unixTimestamp);
  const dateString = new Intl.DateTimeFormat("en-US", {
    year: "numeric",
    month: "short",
    day: "numeric",
    timeZone: "UTC",
  }).format(expireDate);
  const timeString = new Intl.DateTimeFormat("en-US", {
    hour: "numeric",
    minute: "numeric",
    second: "numeric",
    hourCycle: "h23",
    timeZone: "UTC",
    timeZoneName: shortTimeZoneName ? "short" : "long",
  }).format(expireDate);
  return `${dateString} at ${timeString}`;
}

export function displayTimestampWithoutDate(
  unixTimestamp: number,
  shortTimeZoneName = true
) {
  const expireDate = new Date(unixTimestamp);
  const timeString = new Intl.DateTimeFormat("en-US", {
    hour: "numeric",
    minute: "numeric",
    second: "numeric",
    hourCycle: "h23",
    timeZoneName: shortTimeZoneName ? "short" : "long",
  }).format(expireDate);
  return timeString;
}


