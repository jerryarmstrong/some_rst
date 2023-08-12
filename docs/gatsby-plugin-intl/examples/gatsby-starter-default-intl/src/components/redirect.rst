examples/gatsby-starter-default-intl/src/components/redirect.js
===============================================================

Last edited: 2020-04-16 02:43:45

Contents:

.. code-block:: js

    import React from "react"
import { injectIntl } from "gatsby-plugin-intl"
import SEO from "../components/seo"

const Redirect = ({ intl }) => {
  return <SEO title={`${intl.formatMessage({ id: "title" })}`} />
}

export default injectIntl(Redirect)


