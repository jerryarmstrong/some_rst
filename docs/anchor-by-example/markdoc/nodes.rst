markdoc/nodes.js
================

Last edited: 2022-08-19 10:41:17

Contents:

.. code-block:: js

    import { Fence } from '@/components/Fence'

const nodes = {
  document: {
    render: undefined,
  },
  th: {
    attributes: {
      scope: {
        type: String,
        default: 'col',
      },
    },
    render: (props) => <th {...props} />,
  },
  fence: {
    render: Fence,
    attributes: {
      language: {
        type: String,
      },
    },
  },
}

export default nodes


