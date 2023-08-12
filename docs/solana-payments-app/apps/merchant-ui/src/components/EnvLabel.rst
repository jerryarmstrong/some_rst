apps/merchant-ui/src/components/EnvLabel.tsx
============================================

Last edited: 2023-08-11 21:51:34

Contents:

.. code-block:: tsx

    export default function EnvLabel() {
    return (
        <div className="bg-red-500 text-white text-xs font-bold p-1 text-center">
            {process.env.NODE_ENV === 'development' && 'Development'}
            {process.env.NODE_ENV === 'test' && 'Staging'}
        </div>
    );
}


