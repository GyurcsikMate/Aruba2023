<script>
	let images = [
		{ name: 'nginx', image: 'https://logo.clearbit.com/nginx.com?size=50' },
		{ name: 'REACT', image: 'https://logo.clearbit.com/react.com?size=50' },
		{ name: 'mysql', image: 'https://logo.clearbit.com/mysql.com?size=50' },
		{ name: 'wordpress', image: 'https://logo.clearbit.com/wordpress.com' },
		{ name: 'mongodb', image: 'https://logo.clearbit.com/mongodb.com' },
		{ name: 'java', image: 'https://logo.clearbit.com/java.com' },
		{ name: 'expressjs', image: 'https://logo.clearbit.com/expressjs.com' },
		{ name: 'laravel', image: 'https://logo.clearbit.com/laravel.com' },
		{ name: 'redhat', image: 'https://logo.clearbit.com/redhat.com' },
		{ name: 'debian', image: 'https://logo.clearbit.com/debian.com' },
		{ name: 'PostgreSQL', image: 'https://logo.clearbit.com/postgreSQL.com' }
	];
</script>

<div class="">
	{#each images as image, index}
		<div class="flex flex-row justify-center outline-primary-500">
			<div class="h-12 mx-2 w-1/4">
				{image.name}-srfgtr
			</div>
			<div class="h-12 mx-2 w-1/6">
				<strong class="text-xl uppercase">{image.name} </strong>
			</div>

			<div class=" h-12 mx-2 w-1/10">
				<button type="button" class="btn variant-filled-error mx-2">STOP</button>
			</div>
			<div class="mx-2 h-12 w-1/10">
				<button type="button" class="btn variant-filled-primary mx-2">Edit</button>
			</div>
			<div class="mx-2 h-12 w-1/10">
				<button type="button" class="btn variant-filled-primary mx-2">Info</button>
			</div>
			<div class="mx-2 h-12 w-1/10">
				<button type="button" class="btn variant-filled-primary mx-2">Restart</button>
			</div>
		</div>
	{/each}
</div>
