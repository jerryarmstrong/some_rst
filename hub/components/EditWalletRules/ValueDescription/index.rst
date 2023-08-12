hub/components/EditWalletRules/ValueDescription/index.tsx
=========================================================

Last edited: 2023-08-11 18:13:34

Contents:

.. code-block:: tsx

    import cx from '@hub/lib/cx';

interface Props {
  className?: string;
  text: React.ReactNode;
}

export function ValueDescription(props: Props) {
  return (
    <div className={cx(props.className, 'text-sm', 'dark:text-neutral-500')}>
      {props.text}
    </div>
  );
}


