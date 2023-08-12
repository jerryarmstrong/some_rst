hooks/useAuth.ts
================

Last edited: 2022-09-30 13:07:41

Contents:

.. code-block:: ts

    import { useSession } from "next-auth/react";
import { useRouter } from "next/router";

export default function useAuth(privatePage: boolean) {
  const router = useRouter();
  const { data, status } = useSession({
    required: privatePage,
    onUnauthenticated() {
      router.push("/");
    },
  });

  return {
    session: data,
    status,
  };
}


