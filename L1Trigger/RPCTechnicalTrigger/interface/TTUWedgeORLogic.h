// $Id: $
#ifndef INTERFACE_TTUWEDGEORLOGIC_H 
#define INTERFACE_TTUWEDGEORLOGIC_H 1

// Include files
#include "L1Trigger/RPCTechnicalTrigger/interface/TTULogic.h"
#include "L1Trigger/RPCTechnicalTrigger/interface/TTUInput.h"

#include <iostream>
#include <vector>

/** @class TTUWedgeORLogic TTUWedgeORLogic.h interface/TTUWedgeORLogic.h
 *  
 *
 *  @author Andres Felipe Osorio Oliveros
 *  @date   2009-08-09
 */
class TTUWedgeORLogic : public TTULogic {
public: 
  /// Standard constructor
  TTUWedgeORLogic( ); 
  
  virtual ~TTUWedgeORLogic( ); ///< Destructor
  
  bool process( const TTUInput & );
  
  void setBoardSpecs( const TTUBoardSpecs::TTUBoardConfig & );
  
protected:
  
private:
  
  bool m_debug;
  
  int m_maxsectors;

  int m_maxwedges;
  
  std::vector<int> m_wedgeSector;
    
};
#endif // INTERFACE_TTUWEDGEORLOGIC_H
