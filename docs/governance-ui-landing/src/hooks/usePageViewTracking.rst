src/hooks/usePageViewTracking.ts
================================

Last edited: 2023-07-18 16:28:32

Contents:

.. code-block:: ts

    import { useEffect } from 'react';

import mixpanel from '@/lib/mixpanel';

export default function usePageViewTracking(name: string) {
  useEffect(() => {
    mixpanel.track('view_page', { name, app: 'marketing' });
  }, [name]);
}


