<style scoped>
    .search {
        padding-top: 24px;
        overflow: hidden;
        zoom: 1;
    }

    .left {
        float: left;
        margin: 0 20px;
        text-align: center;
    }

    .right {
        width: 600px;
        overflow: hidden;
        zoom: 1;
    }

    img {
        padding-top: 4px;
        text-align: center;
    }
</style>

<template>
    <div class="search">
        <div class="left">
            <img src="./../assets/hakuna.png" @click="goHome">
        </div>
        <div class="right">
            <a-input-search
                    v-model="searchText"
                    size="large"
                    @search="searchResult"/>
            <div v-for="item in result" v-bind:key="item.id">
                <searchResult :info="item"></searchResult>
            </div>
        </div>


    </div>
</template>

<script>
    import axios from 'axios'
    import SearchResult from "../components/SearchResult";
    import Logo from "@/components/Logo"

    export default {
        name: "Search",
        data() {
            return {
                searchText: "",
                result: [],
            }
        },
        components: {
            searchResult: SearchResult,
            logo: Logo
        },

        methods: {
            goHome() {
                this.$router.push("/")

            },
            searchResult() {
                if (this.searchText !== '') {
                    this.$router.push({path: `/search`, query: {q: this.searchText}})
                }
                console.info("router query:" + this.$route.query.q)
                console.info("search text: " + this.searchText)


                const path = 'http://localhost:5000/search?q=' + this.$route.query.q;
                axios.get(path)
                    .then((res) => {
                        this.result = res.data;
                        console.info(this.result)

                    })
                    .catch((error) => {
                        // eslint-disable-next-line
                        console.error(error);
                    });
            }
        },

        created() {
            this.searchResult()
        },

        watch: {
            '$route'(to, from) {
                // 对路由变化作出响应...
                this.searchResult()
            }
        }
    }
</script>

