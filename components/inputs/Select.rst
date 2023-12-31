components/inputs/Select.tsx
============================

Last edited: 2023-08-11 18:13:34

Contents:

.. code-block:: tsx

    import { Listbox } from '@headlessui/react'
import { ChevronDownIcon } from '@heroicons/react/solid'
import { StyledLabel, inputClasses } from './styles'
import ErrorField from './ErrorField'
import React from 'react'

/**
 * @deprecated
 * doesn't really have a replacement but needs one
 */
const Select = ({
  value,
  onChange,
  children,
  className = '',
  placeholder = '',
  error = '',
  disabled = false,
  label = '',
  subtitle = '',
  componentLabel,
  useDefaultStyle = true,
  noMaxWidth = false,
  wrapperClassNames = '',
  minWidth = '',
}: {
  value: any | undefined
  onChange: any | undefined
  children: any | undefined
  className?: string | undefined
  placeholder?: string | undefined
  error?: string | undefined
  disabled?: boolean | undefined
  label?: string | undefined
  subtitle?: string | undefined
  componentLabel?: React.ReactNode
  useDefaultStyle?: boolean
  noMaxWidth?: boolean
  wrapperClassNames?: string
  minWidth?: string
}) => {
  return (
    <div
      className={`${wrapperClassNames}`}
      style={minWidth ? { minWidth: minWidth } : {}}
    >
      {label && <StyledLabel>{label}</StyledLabel>}
      {subtitle && <p className="text-fgd-3 mb-1 -mt-2">{subtitle}</p>}
      <div className={`relative ${className} ${error && 'pb-1'}`}>
        <Listbox value={value} onChange={onChange} disabled={disabled}>
          {({ open }) => (
            <>
              <Listbox.Button
                className={inputClasses({
                  className,
                  disabled,
                  error,
                  useDefaultStyle,
                  noMaxWidth,
                })}
              >
                <div
                  className={`flex items-center justify-between text-left ${
                    placeholder ? 'text-fgd-3' : 'text-fgd-1'
                  }`}
                >
                  {componentLabel
                    ? componentLabel
                    : typeof value === 'string'
                    ? value
                    : placeholder}
                  <ChevronDownIcon
                    className={`default-transition flex-shrink-0 h-5 w-5 mr-1 text-primary-light ${
                      open ? 'transform rotate-180' : 'transform rotate-360'
                    }`}
                  />
                </div>
              </Listbox.Button>
              {open ? (
                <Listbox.Options
                  static
                  className={`text-fgd-1 text-sm max-h-64 ${
                    !noMaxWidth && 'max-w-lg'
                  } overflow-auto z-20 w-full p-1 absolute left-0 mt-1 bg-bkg-1 origin-top-left divide-y divide-bkg-3 shadow-lg outline-none rounded-md thin-scroll`}
                >
                  {children}
                </Listbox.Options>
              ) : null}
            </>
          )}
        </Listbox>
        <ErrorField text={error}></ErrorField>
      </div>
    </div>
  )
}

const Option = ({ value, children, className = '' }) => {
  return (
    <Listbox.Option value={value}>
      {({ selected }) => (
        <div
          className={`default-transition px-2 py-3 hover:bg-bkg-2 hover:cursor-pointer text-fgd-2 tracking-wider ${
            selected && `text-primary-light`
          } ${className}`}
        >
          {children}
        </div>
      )}
    </Listbox.Option>
  )
}

Select.Option = Option

export default Select


