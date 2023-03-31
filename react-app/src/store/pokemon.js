const LOAD = 'pokemon/getPokemon'

const load = (pokemon) => {
  return {
    type: LOAD,
    pokemon
  }
}

export const getPokemon = (id) => async dispatch =>{
  const response = await fetch(`/api/pokemon/`)
  if (response.ok){
    const pokemon = await response.json()
    dispatch(load(pokemon))
  }
}

let initialState = {}

const pokemon = (state = initialState, action) => {
  switch (action.type) {
    case LOAD: {
      const newState = {[pokemon.id]: action.pokemon}
      return newState
    }

  }
}

export default pokemon
