<script>
	let images = [
		{ name: 'nginx', image: 'https://logo.clearbit.com/nginx.com' },
		{ name: 'REACT', image: 'https://logo.clearbit.com/react.com' },
		{ name: 'mysql', image: 'https://logo.clearbit.com/mysql.com' },
		{ name: 'wordpress', image: 'https://logo.clearbit.com/wordpress.com' },
		{ name: 'mongodb', image: 'https://logo.clearbit.com/mongodb.com' },
		{ name: 'laravel', image: 'https://logo.clearbit.com/laravel.com' },
		{ name: 'redhat', image: 'https://logo.clearbit.com/redhat.com' },
		{ name: 'debian', image: 'https://logo.clearbit.com/debian.com' },
		{ name: 'PostgreSQL', image: 'https://logo.clearbit.com/postgreSQL.com' },
		{ name: 'java', image: 'https://logo.clearbit.com/java.com' },
		{ name: 'expressjs', image: 'https://logo.clearbit.com/expressjs.com' },
		
	];
</script>

<div class="flex flex-wrap">
	{#each images as image, index}
		<div class=" w-1/4 p-4 justify-center">
			<div class="justify-center text-center">
				<strong class="text-xl uppercase text-center">{image.name}</strong>
				<img class="mx-auto" src={image.image} alt="" />
				<div class="flex row-auto text-center justify-center">
					<button on:click={async () => {
						fetch('http://0.0.0.0:8000/create/nginxv/nginx/81')
							.then((response) => response.text())
							.then((result) => console.log(result))
							.catch((error) => console.log('error', error));
					}} type="button" class="btn variant-filled-primary my-2">Launch</button>
					<button type="button" class="btn variant-filled-warning my-2">Info</button>
				</div>
			</div>
		</div>
	{/each}
</div>
