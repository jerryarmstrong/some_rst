hooks/useProgramVersion.ts
==========================

Last edited: 2023-05-19 22:20:18

Contents:

.. code-block:: ts

    import useWalletStore from 'stores/useWalletStore'

// TODO replace with useProgramVersionQuery
const useProgramVersion = () => {
  // TODO this should really return undefined, not 1, when we don't know the answer yet.
  const queriedVersion = useWalletStore(
    (s) => s.selectedRealm.programVersion as 1 | 2 | 3
  )
  return queriedVersion
}

export default useProgramVersion


