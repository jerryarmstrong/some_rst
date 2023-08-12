src/lib/trackClick.ts
=====================

Last edited: 2023-07-18 16:28:32

Contents:

.. code-block:: ts

    import mixpanel from '@/lib/mixpanel';

export default function trackClick(target: string, context: string) {
  mixpanel.track(
    'click',
    { context, target, app: 'marketing' },
    { transport: 'sendBeacon' }
  );
}


