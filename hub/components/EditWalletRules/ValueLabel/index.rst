hub/components/EditWalletRules/ValueLabel/index.tsx
===================================================

Last edited: 2023-08-11 18:13:34

Contents:

.. code-block:: tsx

    import cx from '@hub/lib/cx';

interface Props {
  className?: string;
  text: string;
}

export function ValueLabel(props: Props) {
  return (
    <div className={cx(props.className, 'font-bold', 'dark:text-neutral-50')}>
      {props.text}
    </div>
  );
}


