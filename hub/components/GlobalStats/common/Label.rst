hub/components/GlobalStats/common/Label.tsx
===========================================

Last edited: 2023-08-11 18:13:34

Contents:

.. code-block:: tsx

    import cx from '@hub/lib/cx';

interface Props {
  className?: string;
  children: string;
}

export function Label(props: Props) {
  return (
    <h2
      className={cx(
        'font-normal',
        'm-0',
        'text-neutral-400',
        'text-sm',
        'uppercase',
        props.className,
      )}
    >
      {props.children}
    </h2>
  );
}


