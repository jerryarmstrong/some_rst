markdoc/nodes.js
================

Last edited: 2023-08-11 10:00:06

Contents:

.. code-block:: js

    import { nodes as defaultNodes } from '@markdoc/markdoc'

import { Fence } from '@/components/Fence'

const nodes = {
  document: {
    render: undefined,
  },
  table: {
    ...defaultNodes.table,
    render: (props) => {
      const Table = defaultNodes.table.render
      return (
        <div className="my-6 overflow-x-auto">
          <Table {...props} />
        </div>
      )
    },
  },
  th: {
    ...defaultNodes.th,
    attributes: {
      ...defaultNodes.th.attributes,
      scope: {
        type: String,
        default: 'col',
      },
    },
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


