clients/js/src/defaultGuards/endDate.ts
=======================================

Last edited: 2023-08-11 23:25:39

Contents:

.. code-block:: ts

    import { getEndDateSerializer, EndDate, EndDateArgs } from '../generated';
import { GuardManifest, noopParser } from '../guards';

/**
 * The endDate guard is used to specify a date to end the mint.
 * Any transaction received after the end date will fail.
 */
export const endDateGuardManifest: GuardManifest<EndDateArgs, EndDate> = {
  name: 'endDate',
  serializer: getEndDateSerializer,
  mintParser: noopParser,
  routeParser: noopParser,
};


