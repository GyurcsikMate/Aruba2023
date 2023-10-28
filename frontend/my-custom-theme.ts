import type { CustomThemeConfig } from '@skeletonlabs/tw-plugin';

export const myCustomTheme: CustomThemeConfig = {
	name: 'my-custom-theme',
	properties: {
		// =~= Theme Properties =~=
		'--theme-font-family-base': `system-ui`,
		'--theme-font-family-heading': `system-ui`,
		'--theme-font-color-base': '0 0 0',
		'--theme-font-color-dark': '255 255 255',
		'--theme-rounded-base': '16px',
		'--theme-rounded-container': '12px',
		'--theme-border-base': '1px',
		// =~= Theme On-X Colors =~=
		'--on-primary': '0 0 0',
		'--on-secondary': '255 255 255',
		'--on-tertiary': '0 0 0',
		'--on-success': '0 0 0',
		'--on-warning': '0 0 0',
		'--on-error': '255 255 255',
		'--on-surface': '255 255 255',
		// =~= Theme Colors  =~=
		// primary | #009EDF
		'--color-primary-50': '217 240 250', // #d9f0fa
		'--color-primary-100': '204 236 249', // #ccecf9
		'--color-primary-200': '191 231 247', // #bfe7f7
		'--color-primary-300': '153 216 242', // #99d8f2
		'--color-primary-400': '77 187 233', // #4dbbe9
		'--color-primary-500': '0 158 223', // #009EDF
		'--color-primary-600': '0 142 201', // #008ec9
		'--color-primary-700': '0 119 167', // #0077a7
		'--color-primary-800': '0 95 134', // #005f86
		'--color-primary-900': '0 77 109', // #004d6d
		// secondary | #333333
		'--color-secondary-50': '224 224 224', // #e0e0e0
		'--color-secondary-100': '214 214 214', // #d6d6d6
		'--color-secondary-200': '204 204 204', // #cccccc
		'--color-secondary-300': '173 173 173', // #adadad
		'--color-secondary-400': '112 112 112', // #707070
		'--color-secondary-500': '51 51 51', // #333333
		'--color-secondary-600': '46 46 46', // #2e2e2e
		'--color-secondary-700': '38 38 38', // #262626
		'--color-secondary-800': '31 31 31', // #1f1f1f
		'--color-secondary-900': '25 25 25', // #191919
		// tertiary | #F85C00
		'--color-tertiary-50': '254 231 217', // #fee7d9
		'--color-tertiary-100': '254 222 204', // #fedecc
		'--color-tertiary-200': '253 214 191', // #fdd6bf
		'--color-tertiary-300': '252 190 153', // #fcbe99
		'--color-tertiary-400': '250 141 77', // #fa8d4d
		'--color-tertiary-500': '248 92 0', // #F85C00
		'--color-tertiary-600': '223 83 0', // #df5300
		'--color-tertiary-700': '186 69 0', // #ba4500
		'--color-tertiary-800': '149 55 0', // #953700
		'--color-tertiary-900': '122 45 0', // #7a2d00
		// success | #84cc16
		'--color-success-50': '237 247 220', // #edf7dc
		'--color-success-100': '230 245 208', // #e6f5d0
		'--color-success-200': '224 242 197', // #e0f2c5
		'--color-success-300': '206 235 162', // #ceeba2
		'--color-success-400': '169 219 92', // #a9db5c
		'--color-success-500': '132 204 22', // #84cc16
		'--color-success-600': '119 184 20', // #77b814
		'--color-success-700': '99 153 17', // #639911
		'--color-success-800': '79 122 13', // #4f7a0d
		'--color-success-900': '65 100 11', // #41640b
		// warning | #EAB308
		'--color-warning-50': '252 244 218', // #fcf4da
		'--color-warning-100': '251 240 206', // #fbf0ce
		'--color-warning-200': '250 236 193', // #faecc1
		'--color-warning-300': '247 225 156', // #f7e19c
		'--color-warning-400': '240 202 82', // #f0ca52
		'--color-warning-500': '234 179 8', // #EAB308
		'--color-warning-600': '211 161 7', // #d3a107
		'--color-warning-700': '176 134 6', // #b08606
		'--color-warning-800': '140 107 5', // #8c6b05
		'--color-warning-900': '115 88 4', // #735804
		// error | #d12711
		'--color-error-50': '248 223 219', // #f8dfdb
		'--color-error-100': '246 212 207', // #f6d4cf
		'--color-error-200': '244 201 196', // #f4c9c4
		'--color-error-300': '237 169 160', // #eda9a0
		'--color-error-400': '223 104 88', // #df6858
		'--color-error-500': '209 39 17', // #d12711
		'--color-error-600': '188 35 15', // #bc230f
		'--color-error-700': '157 29 13', // #9d1d0d
		'--color-error-800': '125 23 10', // #7d170a
		'--color-error-900': '102 19 8', // #661308
		// surface | #5373b0
		'--color-surface-50': '229 234 243', // #e5eaf3
		'--color-surface-100': '221 227 239', // #dde3ef
		'--color-surface-200': '212 220 235', // #d4dceb
		'--color-surface-300': '186 199 223', // #bac7df
		'--color-surface-400': '135 157 200', // #879dc8
		'--color-surface-500': '83 115 176', // #5373b0
		'--color-surface-600': '75 104 158', // #4b689e
		'--color-surface-700': '62 86 132', // #3e5684
		'--color-surface-800': '50 69 106', // #32456a
		'--color-surface-900': '41 56 86' // #293856
	}
};
