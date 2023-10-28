<!-- YOU CAN DELETE EVERYTHING IN THIS PAGE -->

<div class="container h-full mx-auto flex justify-center items-center">
	<div class="space-y-10 text-center flex flex-col items-center">
		<h2 class="h2">Cloud-9</h2>
		<div class="wrap">
			<a href="/" class="tailwind.config.ts">
				<!-- Tile Content Goes Here -->
				<span>Text</span>
			</a>

			<a href="/" class="tile tile-medium">
				<!-- Tile Content Goes Here -->
				<span>Text</span>
			</a>

			<a href="/" class="tile tile-large">
				<!-- Tile Content Goes Here -->
				<span>Text</span>
			</a>
		</div>
		<!-- / -->
		<div class="flex justify-center space-x-2">
			<button
				class="btn variant-filled"
				on:click={async () => {
					let data = await fetch('http://0.0.0.0:8000/list');

					console.log(data);
				}}
			>
				varazslat
			</button>
			<button
				class="btn variant-filled"
				on:click={async () => {
					fetch('http://0.0.0.0:8000/list')
						.then((response) => response.text())
						.then((result) => console.log(result))
						.catch((error) => console.log('error', error));
				}}
			>
				varazslat2
			</button>
		</div>
	</div>
</div>
