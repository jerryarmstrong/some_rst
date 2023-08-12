src/App.test.tsx
================

Last edited: 2022-06-29 05:55:18

Contents:

.. code-block:: tsx

    import React from "react";
import { render, screen } from "@testing-library/react";
import App from "./App";

test("renders learn react link", () => {
  render(<App />);
  const linkElement = screen.getByText(/learn react/i);
  expect(linkElement).toBeInTheDocument();
});


