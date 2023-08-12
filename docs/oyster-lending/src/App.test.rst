src/App.test.tsx
================

Last edited: 2021-03-16 20:45:52

Contents:

.. code-block:: tsx

    import React from "react";
import { render } from "@testing-library/react";
import App from "./App";

test("renders learn react link", () => {
  const { getByText } = render(<App />);
  const linkElement = getByText(/learn react/i);
  expect(linkElement).toBeInTheDocument();
});


