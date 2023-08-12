app/popup/pages/app.test.tsx
============================

Last edited: 2020-09-01 18:17:54

Contents:

.. code-block:: tsx

    import React from "react"
import { render } from "@testing-library/react"
import { App } from "./app"

test("renders learn react link", () => {
  const { getByText } = render(<App />)
  const linkElement = getByText(/learn react/i)
  expect(linkElement).toBeInTheDocument()
})


