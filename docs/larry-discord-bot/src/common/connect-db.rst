src/common/connect-db.ts
========================

Last edited: 2022-11-15 02:02:13

Contents:

.. code-block:: ts

    import { connect } from 'mongoose';
import dotenv from 'dotenv';
dotenv.config();
import log from 'loglevel';

export async function connectDatabase(mongoUri: string) {
    await connect(mongoUri);
    log.info('Database Connected!');
}


