<script>
async function getApi() {
    const response = await fetch('http://127.0.0.1:5000/api');
    const data = await response.json();

    if (response.ok)
        return data;
    else
        throw new Error(data);
}

let counter = 0;

function previousRecord() {
    if (counter > 0)
        return counter--;
}

function nextRecord() {
    return counter++;
}

let promise = getApi();
</script>

<main>
  {#await promise}
  <p class="read-the-docs">
    wait...
  </p>
  {:then records}
    {#each Object.entries(records) as record, index}
      <p class="read-the-docs">
        {#if index == counter}
          {record[1]['id']}: {record[1]['title']}
        {/if}
      </p>
    {/each}
  <button on:click={previousRecord}>Previous</button>
  <button on:click={nextRecord}>Next</button>
  {:catch error}
    <p style="color: red">{error}</p>
  {/await}
</main>

<style>
  .read-the-docs {
    color: #888;
  }
</style>
