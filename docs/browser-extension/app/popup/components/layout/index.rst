app/popup/components/layout/index.tsx
=====================================

Last edited: 2020-09-01 18:17:54

Contents:

.. code-block:: tsx

    import React from "react"
import { Layout } from "./layout"

export function withLayout<T>(Component: React.ComponentType<T>): React.ComponentType<T> {
  return (props: T) => {
    return (
      <Layout>
        <Component {...props} />
      </Layout>
    )
  }
}


