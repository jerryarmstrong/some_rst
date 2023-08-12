components/inputs/ErrorField.tsx
================================

Last edited: 2023-05-19 22:20:18

Contents:

.. code-block:: tsx

    import { capitalize } from '@utils/helpers'

const ErrorField = ({ text }) => {
  return text ? (
    <div className="text-red text-xs">{text ? capitalize(text) : text}</div>
  ) : null
}

export default ErrorField


