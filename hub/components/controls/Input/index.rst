hub/components/controls/Input/index.tsx
=======================================

Last edited: 2023-08-11 18:13:34

Contents:

.. code-block:: tsx

    import cx from '@hub/lib/cx';

interface Props extends React.InputHTMLAttributes<HTMLInputElement> {}

export function Input(props: Props) {
  const { className, ...rest } = props;

  return (
    <input
      className={cx(
        'bg-zinc-50',
        'border-zinc-300',
        'border',
        'h-14',
        'px-3',
        'outline-none',
        'rounded-md',
        'text-neutral-900',
        'transition-colors',
        'hover:border-zinc-400',
        'focus:border-sky-500',
        'placeholder:text-neutral-400',
        'dark:bg-neutral-800',
        'dark:border-neutral-700',
        'dark:placeholder:text-neutral-600',
        'dark:text-neutral-50',
        'disabled:opacity-50',
        'disabled:pointer-events-none',
        className,
      )}
      {...rest}
    />
  );
}


