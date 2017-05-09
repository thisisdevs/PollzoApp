$(".int-btn").on('click',function(event){
  event.preventDefault();
  console.log("clicked");
  element = $(this);
  $.ajax({
    url:'/user/ajaxrequest/followinterest/',
    data:{
      intId : element.attr("data-id")
    },
    success : function(response){
      if(response == 1){
        element.removeClass("btn-primary");
        element.addClass("btn-danger");
        element.html("Unfollow");
      }
      else if(response == 2){
        element.removeClass("btn-danger");
        element.addClass("btn-primary");
        element.html("Follow");
      }
    }
  });
})

$('.photo-tile').on('click',function(event){
  console.log("clicked");
  event.preventDefault();
  element = $(this);
  $(".panel-success").removeClass('panel-success').addClass("panel-primary");
  element.removeClass('panel-primary').addClass('panel-success');
  $.ajax({

    url:'/user/ajaxrequest/changecover/',
    data:{
      photoId:element.attr('data-id')
    },
    success:function(response){
      $(".header").css({
        'background-image':'url('+response+')'
      });
    }
  });

})

$('.f-btn').on('click',function(event){
  console.log('clicked');
  event.preventDefault();
  element = $(this)
  $.ajax({
    url:'/user/ajaxrequest/followuser',
    data:{
      userId:element.attr('data-id')
    },
    success:function(response){
      if(response==1){
        element.removeClass("btn-primary").addClass("btn-danger");
        element.html("<span class='glyphicon glyphicon-remove-sign'></span>&nbsp;Unfollow");
      }
      else if(response==2){
      element.removeClass("btn-danger").addClass("btn-primary");
      element.html("<span class='glyphicon glyphicon-ok-sign'></span>&nbsp;Follow");
    }
  }
  });
})

$('.choice-box').on('click',function(event){
  element = $(this)
  console.log('clicked');
  $.ajax({
    url:'/user/ajaxrequest/vote/',
    data: {
      qID : element.attr('data-q'),
      cID : element.attr('data-c')
    },
    success:function(response){
      console.log(response);
      if(response!=0){
        element.css({
          'background-color':'#697f4d',
          'color':'white'
        });
        element.find('.vote-count').html(response.toString());
      }
      else{
        element.parent().parent().find('.panel-footer').append('<p style="color:red;">you can\'t change your vote</p>').delay(5000).find('p').fadeOut(1000);
      }
    }
  });
})


$('.delete-poll-btn').on('click',function(event){
  element = $(this)
  console.log('clicked');
  $.ajax({
    url:'/user/ajaxrequest/delete/',
    data: {
      qID : element.attr('data-q')

    },
    success:function(response){
      console.log(response);
      if(response!=0){
        element.parent().parent().parent().remove()
      }
    }
  });
})
