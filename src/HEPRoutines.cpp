#include "HEPHero.h"

//---------------------------------------------------------------------------------------------
// Pre-Routines Setup
//---------------------------------------------------------------------------------------------
void HEPHero::PreRoutines() {
    
    //=============================================================================================
    // CMS SETUP
    //=============================================================================================

    //----OUTPUT INFO------------------------------------------------------------------------------
    _outputTree->Branch( "evtWeight", &evtWeight );
    HDF_insert( "evtWeight", &evtWeight );

}


//---------------------------------------------------------------------------------------------
// On fly Routines Setup [run before genWeight count]
//---------------------------------------------------------------------------------------------
bool HEPHero::RunRoutines() {
    
    //======SUM THE GENERATOR WEIGHTS=================================================
    if( dataset_group != "Data" ){
        SumGenWeights_original += genWeight;
        SumGenWeights += genWeight;
    }


    //======MC SAMPLES PROCESSING=====================================================
    if( !MC_processing() ) return false;


    //======START EVENT WEIGHT========================================================
    evtWeight = 1.;
    if( dataset_group != "Data" ) evtWeight = genWeight;

    
    return true;
}


//---------------------------------------------------------------------------------------------
// MCsamples processing
//---------------------------------------------------------------------------------------------
bool HEPHero::MC_processing(){

    bool pass_cut = true;
    string dsName = _datasetName.substr(0,_datasetName.length()-5);



    return pass_cut;
}

    
