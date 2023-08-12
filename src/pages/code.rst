src/pages/code.tsx
==================

Last edited: 2023-07-18 16:28:32

Contents:

.. code-block:: tsx

    import { useRouter } from 'next/router';
import { useEffect } from 'react';

export default function Code() {
  const router = useRouter();

  useEffect(() => {
    router.replace('https://app.realms.today/code');
  }, [router]);

  return null;
}


