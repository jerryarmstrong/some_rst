src/with-intl.js
================

Last edited: 2020-04-16 02:43:45

Contents:

.. code-block:: js

    import React from "react"
import { injectIntl } from "react-intl"
export default Component => props => {
  console.warn("withIntl is deprecated. Please use injectIntl instead.")
  return React.createElement(injectIntl(Component), props)
}


