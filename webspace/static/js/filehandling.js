// initialize variables
var files = {},
    BYTE = 1,
    KILOBYTE = 1024 * BYTE,
    MEGABYTE = KILOBYTE * KILOBYTE;

// using jQuery
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');

function fileSizeToStr( size ){
  if( size < KILOBYTE ){
    // if the size is less than 1024, it's in the byte range
    return size + ' B';
  }
  else if( size > KILOBYTE && size < MEGABYTE ){
    // if the file size is in the range of Kilobytes
    return (size / KILOBYTE).toFixed( 1 ) + ' KB';
  }
  else if( size > MEGABYTE ){
    return (size / MEGABYTE).toFixed( 1 ) + ' MB';
  }
}

function addFiles( fs ){
  if( typeof fs !== 'undefined'){
    for( i = 0; i < fs.length; i++ ){
      // does the current filename already exist?
      if( !files[ fs[ i ].name ] ){
        // add the current file to the list
        // of files to upload
        files[ fs[ i ].name ] = fs[ i ];
        // copy the table template
        var tr = $( '#template_table' ).find( 'tr' ).clone( true,true );
        // add the name
        tr.find( '.filename' ).html( fs[ i ].name );
        // add the filesize
        tr.find( '.filesize' ).html( fileSizeToStr( fs[ i ].size ) );
        // append to the table
        $( '#file_list' ).append( tr );
      }
      else{
        alert( "A file with the name '" + fs[ i ].name + "' has already been selected." );
      }
    }
  }
}
function drop( evt ) {
    handleDragOver( evt );
    fs = evt.originalEvent.dataTransfer.files;
    addFiles( fs );
}

function handleDragOver( evt ) {
    evt.originalEvent.stopPropagation();
    evt.originalEvent.preventDefault();
}

$(document).ready(function(){
    // Setup the dnd handler
    $( '#drop_file' )
        .bind( 'dragenter', handleDragOver )
        .bind( 'dragover', handleDragOver )
        .bind( 'drop', drop );
        
    // set up the upload button handler
    $('#upload_files').bind( 'change', function(){
      addFiles( this.files );
    } );
    
    // remove file handler
    $( '.remove_file' ).click( function(){
      var x = confirm( "Are you sure you want to remove this file?" );
      if( x ){
        var filename = $( this ).parent().siblings( '.filename' ).text();
        delete files[ filename ];
        $( this ).parents( 'tr' ).remove();
      }
    } );
    
    // upload button handler
    $('#upload_button').click( function( e ){
      e.preventDefault();
      form = new FormData();
      // keep track of the number of files
      // we don't want to send an empty list
      var filecount = 0;
      // loop over the files in the dict
      for( file in files ){
        // if the files object has the name of the file
        // as an actual property
        if( files.hasOwnProperty( file ) ){
          // increment the number of files
          filecount++;
          // add the filename, file object to the form
          form.append( file, files[ file ] );
        }
      }
      // for csrf purposes, add the token
      form.append( 'csrfmiddlewaretoken', csrftoken );
      // keyword for file upload
      form.append( 'fileupload', '' );
      if( filecount > 0 ){
        $.ajax( {
          url: FILE_URL,
          type: "POST",
          data: form,
          // tell jQuery not to process the data
          processData: false,
          // tell jQuery not to set contentType
          contentType: false 
        } ).done( function( e ){
          if( e.error ){
            alert( e.message );
          }
          else{
            window.location = USERS_FILES
          }
        } ).fail( function( e ){
          if( filename > 1 ){
            alert( "An error has occurred and your files have not been uploaded" );
          }
          else{
            alert( "An error has occurred and your file has not been uploaded" );
          }
        } );
      }
      else{
        alert("No files to upload!")
      }
    } );
});
