hub/components/Hub/Roadmap/CompletedSvg.tsx
===========================================

Last edited: 2023-05-19 22:20:18

Contents:

.. code-block:: tsx

    interface Props extends React.SVGAttributes<SVGElement> {}

export function CompletedSvg(props: Props) {
  return (
    <svg {...props} viewBox="0 0 33 33" xmlns="http://www.w3.org/2000/svg">
      <path
        fillRule="evenodd"
        clipRule="evenodd"
        d="M8.72575 5.72574C10.7879 3.66361 13.5837 2.50355 16.5 2.5C19.4163 2.50355 22.2121 3.66361 24.2743 5.72574C26.3364 7.78787 27.4965 10.5837 27.5 13.5C27.5036 15.8822 26.7255 18.1997 25.2852 20.0972L25.2837 20.0996C25.2837 20.0996 24.9834 20.4941 24.939 20.5474L16.5 30.5L8.06451 20.5517C8.01631 20.4945 7.71631 20.1 7.71631 20.1C6.27515 18.2018 5.49657 15.8833 5.50001 13.5C5.50356 10.5837 6.66362 7.78787 8.72575 5.72574ZM20.2515 10.75L15.3751 15.625L12.7515 13L11.2515 14.5L15.3751 18.625L21.7515 12.25L20.2515 10.75Z"
      />
    </svg>
  );
}


