components/instructions/InstructionDataView.tsx
===============================================

Last edited: 2023-08-11 18:13:34

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


