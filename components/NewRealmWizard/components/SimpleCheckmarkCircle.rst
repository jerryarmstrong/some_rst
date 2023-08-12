components/NewRealmWizard/components/SimpleCheckmarkCircle.tsx
==============================================================

Last edited: 2023-08-11 18:13:34

Contents:

.. code-block:: tsx

    export default function ({ selected = false }) {
    return (
      <div
        className={`h-[16px] w-[16px] rounded-full flex items-center justify-center ${
          selected
            ? 'bg-fgd-1 border border-bkg-1'
            : 'border border-fgd-3'
        } group-disabled:text-fgd-4 group-disabled:group-hover:border-fgd-4 group-disabled:hover:border-fgd-4`}
      >
        {selected &&
          <div className="w-2 h-2 border-0 bg-bkg-1 rounded-full"></div>
        }
      </div>
    )
  }
  

