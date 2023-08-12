hooks/useQueryContext.tsx
=========================

Last edited: 2023-05-19 22:20:18

Contents:

.. code-block:: tsx

    import { useRouter } from 'next/router'
import { EndpointTypes } from '../models/types'

export default function useQueryContext() {
  const router = useRouter()
  const { cluster, viewAs } = router.query

  const endpoint = cluster ? (cluster as EndpointTypes) : 'mainnet'
  const hasClusterOption = endpoint !== 'mainnet'
  const fmtUrlWithCluster = (url: string) => {
    const urlWithCluster = hasClusterOption
      ? decodeURIComponent(
          `${url}${url.includes('?') ? '&' : '?'}cluster=${endpoint}`
        )
      : url

    // apologies for the overly verbose code
    const urlWithViewAs =
      typeof viewAs === 'string'
        ? decodeURIComponent(
            `${urlWithCluster}${
              urlWithCluster.includes('?') ? '&' : '?'
            }viewAs=${viewAs}`
          )
        : urlWithCluster

    return urlWithViewAs
  }

  return {
    fmtUrlWithCluster,
  }
}


