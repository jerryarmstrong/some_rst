hub/components/GlobalHeader/User/Loading.tsx
============================================

Last edited: 2023-05-19 22:20:18

Contents:

.. code-block:: tsx

    import cx from '@hub/lib/cx';

interface Props {
  className?: string;
  compressed?: boolean;
}

export function Loading(props: Props) {
  return (
    <div
      className={cx(
        props.className,
        'animate-pulse',
        'bg-neutral-200',
        'cursor-pointer',
        'flex',
        'items-center',
        'justify-center',
        'py-2',
        'rounded',
        'transition-colors',
        props.compressed ? 'w-[68px]' : 'w-48',
      )}
    >
      &nbsp;
    </div>
  );
}


