pages/api/splGovernancePrograms.api.ts
======================================

Last edited: 2023-08-11 18:13:34

Contents:

.. code-block:: ts

    import { withSentry } from '@sentry/nextjs'
import { NextApiRequest, NextApiResponse } from 'next'
import { getAllSplGovernanceProgramIds } from './tools/realms'

// Returns unique spl-governance program ids
const handler = (req: NextApiRequest, res: NextApiResponse) => {
  const cluster = req.query.cluster?.toString() || undefined
  res.status(200).json(getAllSplGovernanceProgramIds(cluster))
}

export default withSentry(handler)


