<template>
    <div class="home">

        <logo class="ha"></logo>
        <div class="search-input">
            <a-input-search
                    size="large"
                    placeholder="在 hakuna 上搜索电影"
                    v-focus v-model="searchText"
                    @search="onSearch"/>
        </div>


        </a-row>

    </div>
</template>

<script>
    // @ is an alias to /src
    import Logo from "@/components/Logo.vue"

    export default {
        name: 'home',
        data() {
            return {
                searchText: ""
            };
        },
        components: {
            logo: Logo,
        },
        methods: {
            onSearch() {
                if (this.searchText !== '') {
                    this.$router.push({path: `/search`, query: {q: this.searchText}})
                    console.info("home router q  :" + this.searchText)
                }
            }
        },
        directives: {
            focus: {
                inserted: function (el) {
                    el.focus();
                }
            }
        }
    }
</script>

<style scoped>
    .home {
        position:absolute;
        left:50%;    /* 定位父级的50% */
        top:50%;
        transform: translate(-50%,-50%); /*自己的50% */
    }
    .search-input{
        width: 600px;
    }
    .ha {
        text-align: center;
    }

</style>
