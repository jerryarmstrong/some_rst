app/popup/context/connection.tsx
================================

Last edited: 2020-09-01 18:17:54

Contents:

.. code-block:: tsx

    import React, { useContext, useMemo } from "react"
import { Connection } from "@solana/web3.js"
import { useBackground } from "./background"

interface ConnectionContextType {
  connection: Connection
}

const ConnectionContext = React.createContext<ConnectionContextType>(null!)

export function ConnectionProvider(props: React.PropsWithChildren<{}>) {
  const { popupState } = useBackground()
  const endpoint = popupState?.selectedNetwork.endpoint ?? ""
  const connection = useMemo<Connection>(() => new Connection(endpoint, "single"), [endpoint])

  return (
    <ConnectionContext.Provider value={{ connection }}>{props.children}</ConnectionContext.Provider>
  )
}

export const useConnection = (): ConnectionContextType => {
  const context = useContext(ConnectionContext)
  if (!context) {
    throw new Error(
      "Connection not found, useConnection must be used within the <ConnectionProvider>..</ConnectionProvider>"
    )
  }
  return context
}


