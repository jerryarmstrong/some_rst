templates/docs/gatsby/gatsby-ssr.js
===================================

Last edited: 2021-10-02 02:46:04

Contents:

.. code-block:: js

    /**
 * Implement Gatsby's Browser APIs in this file.
 *
 * See: https://www.gatsbyjs.org/docs/browser-apis/
 */

// You can delete this file if you're not using it
import React from "react"
import { ReusableProvider } from "reusable"

export const wrapRootElement = ({ element }) => (
  <ReusableProvider>{element}</ReusableProvider>
)


