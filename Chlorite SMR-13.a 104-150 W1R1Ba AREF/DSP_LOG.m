function DSP_LOG( actionString , arg1 , arg2 , arg3 , arg4 , arg5 , arg6 )
global DSP_LOG_FIGIMG_CNT
oriDirectory = cd;
if( strcmp( actionString , 'log fig and img' ) == 1 )
    % arg1 = filePointer ;
    % arg2 = folderName ; 
    % arg3 = objectName ;
    % arg4 = objectExtension;
            % ============================================
            % check arg4 for fig , or png , or fig and png
            % ============================================
            if ( strcmp( arg4 , 'fig and png' ) )
                logBothFlag = 1;
            else
                logBothFlag = 0;
            end
    
    dos( [ 'if not exist ' , arg2 , ' ( md ' , arg2 , ' )' ] );
    cd(arg2);
    if ( DSP_LOG_FIGIMG_CNT < 10 )
        if ( logBothFlag == 0 )
            saveas( arg1 , [ '0' , int2str(DSP_LOG_FIGIMG_CNT) , '_' arg3 ] , arg4 );
        else % else means it is to log both fig and bmp
            saveas( arg1 , [ '0' , int2str(DSP_LOG_FIGIMG_CNT) , '_' arg3 ] , 'fig' );
            saveas( arg1 , [ '0' , int2str(DSP_LOG_FIGIMG_CNT) , '_' arg3 ] , 'png' );
        end
    else % else means it is 11 or 12 or larger , no need to preadd '0' at the front
        if ( logBothFlag == 0 )
            saveas( arg1 , [ int2str(DSP_LOG_FIGIMG_CNT) , '_' arg3 ] , arg4 );
        else % else means it is to log both fig and bmp
            saveas( arg1 , [ int2str(DSP_LOG_FIGIMG_CNT) , '_' arg3 ] , 'fig' );
            saveas( arg1 , [ int2str(DSP_LOG_FIGIMG_CNT) , '_' arg3 ] , 'png' );
        end
    end
    DSP_LOG_FIGIMG_CNT = DSP_LOG_FIGIMG_CNT + 1;
    if( ~strcmp( arg2 , '.' ) )
        cd(oriDirectory);
    end
end
if( strcmp( actionString , 'log matrix to txt' ) )
    %dlmwrite(filename, M)
    %dlmwrite(filename, M, 'D')
    %dlmwrite(filename, M, 'D', R, C)
    % arg1 = folderName
    % arg2 = txtFileName
    % arg3 = matrix
    % arg4 = delims
    % arg5 = start from which row | first row is notated by 0
    % arg6 = start from which column | first column is notated by 0
    dos( [ 'if not exist ' , arg1 , ' ( md ' , arg1 , ' )' ] );
    cd(arg1);
    dlmwrite( arg2 , arg3 , arg4 );
    if( ~strcmp( arg1 , '.' ) )
        cd(oriDirectory);
    end
end
if( strcmp( actionString , 'log plot' ) )
	% arg1 = filePointer
	% arg2 = folderName
	% arg3 = objectName
	% arg4 = objectExtension
            % ============================================
            % check arg4 for fig , or png , or fig and png
            % ============================================
            if ( strcmp( arg4 , 'fig and png' ) )
                logBothFlag = 1;
            else
                logBothFlag = 0;
            end
	dos( [ 'if not exist ' , arg2 , ' ( md ' , arg2 , ' )' ] );
	cd(arg2);
	if ( logBothFlag == 0 )
		saveas( arg1 , arg3 , arg4 );
	else % else means it is to log both fig and bmp
		saveas( arg1 , arg3 , 'fig' );
		saveas( arg1 , arg3 , 'png' );
	end
	if( ~strcmp( arg2 , '.' ) )
        cd(oriDirectory);
    end
end