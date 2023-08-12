backend/native/xnft-api-server/src/v1/index.ts
==============================================

Last edited: 2023-07-01 03:20:04

Contents:

.. code-block:: ts

    import express from "express";
const router = express.Router();
import notificationRouter from "./notifications";
import userRoutes from "./users";
import xnftRoutes from "./xnft";

router.use("/notifications", notificationRouter);
router.use("/users", userRoutes);
router.use("/xnft", xnftRoutes);

export default router;


