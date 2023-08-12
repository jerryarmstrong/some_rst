components/instructions/InstructionDataView.tsx
===============================================

Last edited: 2023-05-19 22:20:18

Contents:

.. code-block:: tsx

    import { InstructionDescriptor } from './tools'

const InstructionDataView = ({
  descriptor,
}: {
  descriptor: InstructionDescriptor | undefined
}) => {
  return (
    <div>
      <span className="break-all font-display text-fgd-1 text-xs">
        {descriptor?.dataUI}
      </span>
    </div>
  )
}

export default InstructionDataView


