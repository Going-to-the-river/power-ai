import Vue from "vue";

export default {
  async is_error(data, root_state, context){
    var account = root_state.account

    if (data.hasOwnProperty('error')){
      var error = data.error

      if(error === 'token expired'){
        if(account.is_logged_in){
          if(account.is_tmp_user){
            alert('Время анонимной сессии истекло! Корзина очищена')
          }else{
            alert('Время пользовательской сессии истекло! Произведен выход из аккаунта')
          }
          await context.dispatch('logout')
        }else{
          console.log('Oops, that is strange. Not logged in account but got "token expired" error')
        }
        return true

      }else if(error === 'wrong token'){
        if(account.is_logged_in){
          if(account.is_tmp_user){
            alert('Сбой анонимной сессии! Корзина очищена')
          }else{
            alert('Сбой пользовательской сессии! Произведен выход из аккаунта')
          }
          await context.dispatch('logout')
        }else{
          //occurs on failed login
          //pass
        }
        return true
      }else{
        console.log(data.error)
        return false
      }
    }
    return false
  },

  //~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
}

