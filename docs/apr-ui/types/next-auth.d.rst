types/next-auth.d.ts
====================

Last edited: 2022-09-30 13:07:41

Contents:

.. code-block:: ts

    import { DefaultSession } from "next-auth";

declare module "next-auth" {
  interface Session {
    user: {
      accessToken: string;
      id: string;
      picture: number;
    } & DefaultSession["user"];
  }
}


