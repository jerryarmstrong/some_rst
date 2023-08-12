backend/native/backpack-api/src/routes/v1/__tests__/referrals.test.ts
=====================================================================

Last edited: 2023-07-01 03:20:04

Contents:

.. code-block:: ts

    import { expect, test } from "vitest";

import { API_URL, sol_only } from "./_constants";

test("referring a user sets a referrer cookie and redirect to chrome store", async () => {
  const res = await fetch(`${API_URL}/referrals/sol_only`, {
    redirect: "manual",
  });
  expect(res.headers.get("set-cookie")).toContain(`referrer=${sol_only.id};`);
  expect(res.status).toBe(302);
  expect(res.headers.get("location")).toEqual(
    "https://chrome.google.com/webstore/detail/backpack/aflkmfhebedbjioipglgcbcmnbpgliof"
  );
});


