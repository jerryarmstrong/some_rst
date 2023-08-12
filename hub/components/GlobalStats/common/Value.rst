hub/components/GlobalStats/common/Value.tsx
===========================================

Last edited: 2023-08-11 18:13:34

Contents:

.. code-block:: tsx

    import cx from '@hub/lib/cx';

interface Props {
  className?: string;
  children: string;
}

export function Value(props: Props) {
  return (
    <div
      className={cx(
        'font-medium',
        'text-5xl',
        'text-neutral-900',
        'w-48',
        props.className,
      )}
    >
      {props.children}
    </div>
  );
}


