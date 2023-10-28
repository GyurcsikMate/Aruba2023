<script lang="ts">
	import '../app.postcss';
	import { AppShell, AppBar } from '@skeletonlabs/skeleton';

	// Floating UI for Popups
	import { computePosition, autoUpdate, flip, shift, offset, arrow } from '@floating-ui/dom';
	import { storePopup } from '@skeletonlabs/skeleton';
	import Navigation from '$lib/components/Navigation.svelte';
	storePopup.set({ computePosition, autoUpdate, flip, shift, offset, arrow });
</script>

<!-- App Shell -->
<AppShell slotSidebarLeft="w-52 bg-surface-400 p-4" slotHeader="bg-surface-300">
	<svelte:fragment slot="header">
		<!-- App Bar -->
		<AppBar background="bg-surface-300">
			<svelte:fragment slot="lead">
				<strong class="text-xl uppercase"><img class="w-60" src="/LOGO.png" /></strong>
			</svelte:fragment>
			<svelte:fragment slot="trail">
				<a class="btn btn-sm variant-ghost-surface" href="/"> Home </a>
				<a class="btn btn-sm variant-ghost-surface" href="/marketplace"> Marketplace </a>
				<a class="btn btn-sm variant-ghost-surface" href="/dashboard"> Dashboard </a>
				<a class="btn btn-sm variant-ghost-surface" href="https://github.com/skeletonlabs/skeleton">
					Q&A
				</a>
			</svelte:fragment>
		</AppBar>
	</svelte:fragment>
	<svelte:fragment slot="sidebarLeft">
		<Navigation />
	</svelte:fragment>
	<!-- Page Route Content -->
	<div class="container p-10 mx-auto">
		<slot />
	</div>
</AppShell>
