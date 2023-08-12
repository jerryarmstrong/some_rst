components/inputs/ErrorField.tsx
================================

Last edited: 2023-08-11 18:13:34

Contents:

.. code-block:: tsx

    import { capitalize } from '@utils/helpers'

const ErrorField = ({ text }) => {
  return text ? (
    <div className="text-red text-xs">{text ? capitalize(text) : text}</div>
  ) : null
}

export default ErrorField


